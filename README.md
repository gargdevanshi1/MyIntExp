# 📘 Student Interview Experience Forum

A Django-based web application that provides a structured and user-friendly platform for students to **share and access past interview experiences** across a wide range of job profiles. It aims to reduce time spent searching for reliable resources by offering a centralized, moderated space for peer-contributed insights.

---

## 💡 Problem Statement

The internet is filled with unstructured and often unreliable information regarding job interviews. Students frequently waste time finding relevant, genuine experiences. This project solves that by creating a **student-centric forum** to:

- Upload and access categorized interview experiences
- View personal contribution history
- Ensure content quality through moderator approvals

---

## 🛠️ Tech Stack

- **Backend**: Python, Django  
- **Frontend**: HTML, CSS, Bootstrap, JavaScript  
- **Database**: SQLite (default Django DB)  

---

## 🧱 Features & Pages

### 🔐 Login Page
- **Student Login**: Access the forum and personal profile.
- **Moderator Login**: Review and approve interview submissions (Superuser access).

### 📝 Registration Page
- New students register via a form capturing personal details.
- Post-registration, users are redirected to the login page.

### 🗂️ Forum Page
- View past interview experiences categorized by job roles:
  - Business Analyst
  - Operations Analyst
  - Marketing Manager
  - Software Developer
  - Data Analyst
  - System Engineer
  - Data Scientist
- Access to profile and logout functionality.

### 🙋‍♂️ My Profile Page
- Displays the student’s personal information.
- Shows all experiences previously uploaded.
- Option to upload new experiences.

### ➕ Add Experience Page
- Submit a new interview experience with:
  - Selected job profile
  - Description of each round
- Redirects to My Profile upon submission.

### 📄 Experience Details Page
- View full content of a selected interview experience.
- **Moderator View**: Includes checkbox to approve/reject before publication.

---

## 🔐 User Roles

- **Student**
  - Register, log in, view & upload interview experiences
  - Edit personal profile and view contribution history

- **Moderator (Admin/Superuser)**
  - Log in via separate route
  - View unapproved submissions
  - Approve/reject experiences for publishing

---
