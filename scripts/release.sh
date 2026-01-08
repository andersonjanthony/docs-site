#!/bin/bash

# SBS Release Script
# Usage: npm run release <version>
# Example: npm run release 0.1.1

if [ -z "$1" ]; then
  echo "❌ Error: Version number required"
  echo "Usage: npm run release <version>"
  echo "Example: npm run release 0.1.1"
  exit 1
fi

VERSION=$1

echo "🚀 Releasing SBS v${VERSION}..."
echo ""

# Update VERSION file
echo "${VERSION}" > VERSION
echo "✅ Updated VERSION file to ${VERSION}"

# Stage VERSION file
git add VERSION
echo "✅ Staged VERSION file"

# Commit
git commit -m "Release v${VERSION}"
echo "✅ Committed release"

# Create tag
git tag "v${VERSION}"
echo "✅ Created tag v${VERSION}"

# Push commit
git push origin main
echo "✅ Pushed to main branch"

# Push tag
git push origin "v${VERSION}"
echo "✅ Pushed tag v${VERSION}"

echo ""
echo "🎉 Release v${VERSION} complete!"
echo "📦 GitHub Actions will now build and publish the release"
echo "🔗 Check: https://github.com/yourusername/sbs/releases/tag/v${VERSION}"

