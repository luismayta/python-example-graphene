#!/usr/bin/env bash
# -*- coding: utf-8 -*-

# shellcheck source=/dev/null
[ -r "script/bootstrap.sh" ] && source "script/bootstrap.sh"

cd "${SOURCE_DIR}" || echo 'Not Found'

python manage.py runserver "${APP_IP}:${APP_PORT}"
