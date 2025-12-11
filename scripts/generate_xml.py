#!/usr/bin/env python3
"""
Generate XML representation of SBS controls from markdown files.
"""

import os
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom
from pathlib import Path

def parse_control_from_lines(lines, start_idx):
    """Parse a single control starting from the given line index."""
    control = {}
    current_field = None
    current_content = []
    
    i = start_idx
    while i < len(lines):
        line = lines[i]
        
        # Check if we've hit the next control or end
        if line.startswith('### SBS-') and i != start_idx:
            break
            
        # Extract control ID and title from header
        if i == start_idx and line.startswith('### SBS-'):
            match = re.match(r'### (SBS-[A-Z]+-\d+):\s*(.+)', line)
            if match:
                control['id'] = match.group(1)
                control['title'] = match.group(2).strip()
        
        # Check for field labels
        elif line.startswith('**Control Statement:**'):
            if current_field and current_content:
                control[current_field] = '\n'.join(current_content).strip()
            current_field = 'statement'
            current_content = [line.replace('**Control Statement:**', '').strip()]
            
        elif line.startswith('**Description:**'):
            if current_field and current_content:
                control[current_field] = '\n'.join(current_content).strip()
            current_field = 'description'
            current_content = [line.replace('**Description:**', '').strip()]
            
        elif line.startswith('**Rationale:**'):
            if current_field and current_content:
                control[current_field] = '\n'.join(current_content).strip()
            current_field = 'rationale'
            current_content = [line.replace('**Rationale:**', '').strip()]
            
        elif line.startswith('**Audit Procedure:**'):
            if current_field and current_content:
                control[current_field] = '\n'.join(current_content).strip()
            current_field = 'audit_procedure'
            current_content = [line.replace('**Audit Procedure:**', '').strip()]
            
        elif line.startswith('**Remediation:**'):
            if current_field and current_content:
                control[current_field] = '\n'.join(current_content).strip()
            current_field = 'remediation'
            current_content = [line.replace('**Remediation:**', '').strip()]
            
        elif line.startswith('**Default Value:**'):
            if current_field and current_content:
                control[current_field] = '\n'.join(current_content).strip()
            current_field = 'default_value'
            current_content = [line.replace('**Default Value:**', '').strip()]
            
        elif line.startswith('**References:**'):
            if current_field and current_content:
                control[current_field] = '\n'.join(current_content).strip()
            current_field = 'references'
            current_content = [line.replace('**References:**', '').strip()]
            
        # Accumulate content for current field
        elif current_field and line.strip():
            current_content.append(line)
            
        i += 1
    
    # Save the last field
    if current_field and current_content:
        control[current_field] = '\n'.join(current_content).strip()
    
    return control, i

def parse_markdown_file(filepath):
    """Parse a markdown file and extract all controls."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    controls = []
    category = None
    category_description = None
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Extract category from ## headers
        if line.startswith('## ') and not line.startswith('###'):
            category = line.replace('##', '').strip()
            # Look ahead for category description
            if i + 2 < len(lines) and lines[i + 2].strip():
                category_description = lines[i + 2].strip()
        
        # Found a control
        elif line.startswith('### SBS-'):
            control, next_idx = parse_control_from_lines(lines, i)
            if control.get('id'):
                control['category'] = category
                control['category_description'] = category_description
                controls.append(control)
            i = next_idx
            continue
            
        i += 1
    
    return controls

def create_xml_element(parent, tag, text=None, attributes=None):
    """Helper to create XML elements with proper formatting."""
    elem = ET.SubElement(parent, tag, attrib=attributes or {})
    if text:
        elem.text = text
    return elem

def generate_xml(controls, version="1.0.0"):
    """Generate XML structure from parsed controls."""
    root = ET.Element('sbs_benchmark')
    root.set('version', version)
    root.set('xmlns', 'https://securitybenchmark.dev/sbs/v1')
    
    # Add metadata
    metadata = ET.SubElement(root, 'metadata')
    create_xml_element(metadata, 'title', 'Security Benchmark for Salesforce')
    create_xml_element(metadata, 'version', version)
    create_xml_element(metadata, 'total_controls', str(len(controls)))
    
    # Group controls by category
    categories = {}
    for control in controls:
        cat = control.get('category', 'Uncategorized')
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(control)
    
    # Add categories and controls
    controls_elem = ET.SubElement(root, 'controls')
    
    for category_name, cat_controls in categories.items():
        category_elem = ET.SubElement(controls_elem, 'category')
        create_xml_element(category_elem, 'name', category_name)
        
        if cat_controls and cat_controls[0].get('category_description'):
            create_xml_element(category_elem, 'description', cat_controls[0]['category_description'])
        
        for control in cat_controls:
            control_elem = ET.SubElement(category_elem, 'control')
            control_elem.set('id', control.get('id', ''))
            
            create_xml_element(control_elem, 'title', control.get('title', ''))
            create_xml_element(control_elem, 'statement', control.get('statement', ''))
            create_xml_element(control_elem, 'description', control.get('description', ''))
            create_xml_element(control_elem, 'rationale', control.get('rationale', ''))
            create_xml_element(control_elem, 'audit_procedure', control.get('audit_procedure', ''))
            create_xml_element(control_elem, 'remediation', control.get('remediation', ''))
            create_xml_element(control_elem, 'default_value', control.get('default_value', ''))
            create_xml_element(control_elem, 'references', control.get('references', ''))
    
    return root

def prettify_xml(elem):
    """Return a pretty-printed XML string."""
    rough_string = ET.tostring(elem, encoding='unicode')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def main():
    """Main function to generate XML from markdown controls."""
    # Get the benchmark directory
    script_dir = Path(__file__).parent
    benchmark_dir = script_dir.parent / 'benchmark'
    output_file = script_dir.parent / 'sbs-controls.xml'
    version_file = script_dir.parent / 'VERSION'
    
    # Read version from VERSION file
    if version_file.exists():
        version = version_file.read_text().strip()
    else:
        version = "0.0.0"
        print("WARNING: VERSION file not found, using 0.0.0")
    
    print(f"SBS Version: {version}")
    print(f"Scanning for controls in: {benchmark_dir}")
    
    # Parse all markdown files
    all_controls = []
    markdown_files = sorted(benchmark_dir.glob('*.md'))
    
    for md_file in markdown_files:
        print(f"Parsing {md_file.name}...")
        controls = parse_markdown_file(md_file)
        all_controls.extend(controls)
        print(f"  Found {len(controls)} control(s)")
    
    print(f"\nTotal controls found: {len(all_controls)}")
    
    # Generate XML
    print("Generating XML...")
    xml_root = generate_xml(all_controls, version=version)
    
    # Write to file
    xml_string = prettify_xml(xml_root)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(xml_string)
    
    print(f"XML written to: {output_file}")
    print("\nControl IDs found:")
    for control in sorted(all_controls, key=lambda x: x.get('id', '')):
        print(f"  - {control.get('id')}: {control.get('title')}")

if __name__ == '__main__':
    main()

