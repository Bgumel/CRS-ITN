
# ITN Distribution System

This is a web-based application for managing ITN (Insecticide-Treated Nets) distribution data. The system allows users to register and log in, submit ITN distribution data, and retrieve distribution records via an API. It is built using Python Django and Django Ninja API.

## Features

- **User Authentication**: Users can register and log in using Django's built-in authentication system.
- **ITN Distribution Data Submission**: Users can submit details about ITN distribution including household ID, household head name, family members, ITNs distributed, and distribution date.
- **API Endpoints**:
  - POST endpoint for submitting ITN distribution data.
  - GET endpoint for retrieving all ITN distribution records.
- **Technical Support Page**: Displays the 3-tier support system for ITN distribution.

## Technologies Used

- **Backend**: Django, Django Ninja API
- **Frontend**: HTML, CSS (styled with CRS ITN brand colors)
- **Database**: SQLite (default, can be changed to any supported by Django)
- **Authentication**: Django's built-in `django.contrib.auth`
  
## Setup Instructions

### Prerequisites

- Python 3.x
- Django
- Ninja API

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Bgumel/CRS-ITN.git
   cd CRS-ITN
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

   The application will now be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).


## API Documentation

The API provides the following endpoints for managing ITN distribution records.

### **POST** `/api/distribution/`

Submit ITN distribution data.

- **Required Fields**:
  - `household_id`: The unique ID of the household.
  - `household_head_name`: Name of the household head.
  - `number_of_family_members`: Total number of family members in the household.
  - `itns_distributed`: Number of ITNs distributed.
  - `distribution_date`: The date of distribution (YYYY-MM-DD).
  - `distributor_id`: The ID of the user distributing the ITNs.

#### Example Request:
```json
{
  "household_id": "123",
  "household_head_name": "John Doe",
  "number_of_family_members": 5,
  "itns_distributed": 3,
  "distribution_date": "2024-09-21",
  "distributor_id": 1
}
```

### **GET** `/api/distributions/`

Retrieve all ITN distribution records in JSON format.

#### Example Response:
```json
[
  {
    "household_id": "HH123",
    "household_head_name": "John Doe",
    "number_of_family_members": 5,
    "itns_distributed": 3,
    "distribution_date": "2024-09-19",
    "distributor_id": 1
    }
  }
]
```

### API Documentation

You can view the API documentation in your browser at [http://127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs).



## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

