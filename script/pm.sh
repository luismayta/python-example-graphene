#!/usr/bin/env bash
# -*- coding: utf-8 -*-

# shellcheck source=/dev/null
[ -r "script/bootstrap.sh" ] && source "script/bootstrap.sh"

cd "${SOURCE_DIR}" || echo 'Not Found'

echo "execute $1"

# python manage
python manage.py "$1"
