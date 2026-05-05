# To-Do Odoo Task Module

A comprehensive task management system module for Odoo that tracks task lifecycles, time efficiency, and team collaboration.

## Project Overview

This Odoo module provides a task management solution designed to help teams organize, track, and manage their work effectively. It integrates with Odoo's built-in chatter and activity features for seamless collaboration.

## Code Architecture

### Project Structure
```
to_do_odoo_task/
├── __manifest__.py          # Module metadata and configuration
├── __init__.py              # Package initialization
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker container configuration
├── docker-compose.yml       # Docker Compose setup for local development
├── README.md                # This file
├── LICENSE                  # LGPL-3 License
├── models/                  # Database models
│   ├── __init__.py
│   ├── to_do.py            # Main task model
│   └── estimated_time.py   # Time tracking model
├── views/                  # UI views and menus
│   ├── base_menu.xml       # Menu configuration
│   ├── to_do_view.xml      # Task view definitions
│   └── estimated_time.xml  # Time tracking view
├── reports/                # Report templates
│   └── todo_reports.xml    # Task reports
└── security/               # Access control
    └── ir.model.access.csv # Model access permissions
```

### Core Models

#### 1. **To-Do Model** (`models/to_do.py`)
- **Purpose**: Main task model for managing project tasks
- **Key Fields**:
  - `name`: Task name (required)
  - `description`: Detailed task description with tracking
  - `due_date`: Task deadline (required, tracked)
  - `status`: Task state (New, In Progress, Completed, Close) - tracked
  - `assign_to`: Assignment to users (Many2one relation)
  - `expected_time`: Estimated time to complete
  - `time_taken`: Computed field - sum of all time entries
  - `remaining_time`: Computed field - expected minus taken time
  - `is_late`: Boolean flag for overdue tasks
  - `active`: Boolean for soft deletion
  
- **Features**:
  - Inherits from `mail.thread` and `mail.activity.mixin` for built-in chatter and activity support
  - Time validation: Ensures actual time doesn't exceed expected time
  - Status actions: Methods to change task status
  - Late detection: Automated check for overdue tasks
  - Computed fields with dependencies for automatic calculations

#### 2. **Estimated Time Model** (`models/estimated_time.py`)
- **Purpose**: Track time spent on task activities
- **Key Fields**:
  - `task_id`: Link to parent task (Many2one relation)
  - `date`: Date of time entry
  - `time_taken`: Hours spent on activity
  - `description`: Activity notes
  - `activity_type`: Type of work (Develop, Check, Meeting)
  - `active`: Boolean for soft deletion

- **Features**:
  - Inherits from `mail.thread` and `mail.activity.mixin`
  - Multiple activity types for granular time tracking
  - Linked to tasks via One2many relationship

### Key Functionality

1. **Task Lifecycle Management**
   - Create tasks with due dates and expected time
   - Assign tasks to team members
   - Track status changes through dedicated actions
   - Automatic late task detection

2. **Time Tracking**
   - Record time spent on various activities
   - Track activity types (development, review, meetings)
   - Automatic calculation of remaining time
   - Validation to prevent time overages

3. **Collaboration**
   - Built-in chatter for task discussions
   - Activity tracking for team awareness
   - Time entry history with notes

4. **Reporting**
   - Task reports (`reports/todo_reports.xml`)
   - Time allocation analysis
   - Status overview

## Dependencies

The module requires:
- **Odoo**: Version 14.0 - 18.0
- **Base Module**: `base` (Odoo core)
- **Mail Module**: `mail` (for chatter and activities)

Python dependencies are listed in `requirements.txt`

## Installation

### Option 1: Using Docker (Recommended)

1. Ensure Docker and Docker Compose are installed
2. Build and start services:
   ```bash
   docker-compose up -d
   ```
3. Access Odoo at `http://localhost:8069`

### Option 2: Manual Installation

1. Install Python dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Install Odoo and add this module to addons path
3. Restart Odoo and install the module from Apps

## Environment Setup

### Create Python Virtual Environment

#### On Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### On Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Database Models Relationships

```
To-Do (to.do)
  └── [1:N] Estimated Time (estimated.time)
       └── Time entries for tracking work
       
To-Do ──[N:1]──> Users (res.users)
       └── Task assignment
```

## Requirements

### Module Features

#### Core Task Management Requirements
![Task Management Requirements](images/requirements_part1.png)

**Key Features:**
- **Lines**: Add field to `todo.task` model "estimated_time". Timesheet lines related to the task, allow users to record all their timesheets in this task. Make sure total times in related lines not exceed estimated time.
- **Archiving Technique**: Add archiving feature to `todo.task` model.
- **Server Action**: Add a server action named "Close" to close tickets (One record or multiple).
- **Cron Job**: Create an automated action related to `todo.task` model to alarm end users that there are late tickets depending on the "Due Date" field, and color these records in the tree view.
- **Report Action**: Users can print any task in a specified design.

#### To-Do Module Configuration
![To-Do Module Requirements](images/requirements_part2.png)

**Core Components:**
- **To-Do Model**: Create a new model named `todo.task` to represent tasks in the to-do list. Include fields such as Task Name, Assign To, Description, Due Date, and Status (New, In Progress, Completed).
- **List View**: Add a menu item under the main menu "To-Do" named "All Tasks". Design a list view to display all the tasks with their key information.
- **Form View**: Create a form view for the `todo.task` model to add and edit tasks. Include form fields for Task Name, Assign To, Description, Due Date, and Status.
- **Search View**: Create a search view for the `todo.task` model to add Status filters and some defaults group by Assign To, Status and Due Date. User also can search with Task Name and Assign To fields.

## Configuration Files

- **`__manifest__.py`**: Module metadata, version, and dependencies
- **`security/ir.model.access.csv`**: Access control rules for models
- **`views/base_menu.xml`**: Menu structure and navigation
- **`views/to_do_view.xml`**: Forms, trees, and search views for tasks
- **`views/estimated_time.xml`**: Views for time tracking

## License

This module is licensed under the LGPL-3 License. See the LICENSE file for details.

## Author

Ahmed
