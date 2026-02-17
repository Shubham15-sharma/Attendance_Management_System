#!/bin/bash
# Attendance Management System - Startup Script
# This script runs the application with proper Tk configuration

cd "$(dirname "$0")"
TK_SILENCE_DEPRECATION=1 python3.11 attendance.py
