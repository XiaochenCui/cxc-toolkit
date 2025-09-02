#!/bin/sh

# 1. pip install twine
# 2. update "VERSION" file
# 3. get the token from https://pypi.org/manage/account/

VERSION=$(cat VERSION)

echo "Publishing version $VERSION"

package() {
    python setup.py bdist_wheel
}

upload() {
    twine upload dist/"cxc_toolkit-$VERSION-py3-none-any.whl"
}

package
upload
