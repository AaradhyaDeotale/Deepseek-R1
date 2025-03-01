import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import TeacherPortal from './components/TeacherPortal';
import StudentPortal from './components/StudentPortal';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <Router>
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <div className="container">
          <Link to="/teacher" className="navbar-brand">Teacher Portal</Link>
          <Link to="/student" className="navbar-brand">Student Portal</Link>
        </div>
      </nav>
      <Routes>
        <Route path="/teacher" element={<TeacherPortal />} />
        <Route path="/student" element={<StudentPortal />} />
      </Routes>
    </Router>
  );
}

export default App;