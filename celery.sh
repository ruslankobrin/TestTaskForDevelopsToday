#!/usr/bin/env bash
celery worker -A TestTaskForDevelopsToday --concurrency=2 --loglevel=INFO --beat -E