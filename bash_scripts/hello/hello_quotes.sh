#!/usr/bin/env bash
# Weak quotes:"

world="World"
echo "Hello $world"

# strong quotes: '
echo 'Hello $world'

# use \ to prevent expansion
echo "Hello \$world"
