import React, { useState } from 'react';
import axios from 'axios';

const StudentPortal = () => {
  const [feedback, setFeedback] = useState('');

  const handleSubmit = async (studentAnswer) => {
    try {
      const response = await axios.post('http://localhost:5000/api/generate-feedback', {
        student_answer: studentAnswer,
        correct_answer: "2 + 2 = 4",
        error_type: "Arithmetic error",
        relevant_notes: "Basic addition rules from Chapter 2"
      });
      setFeedback(response.data.feedback);
    } catch (error) {
      setFeedback('Error generating feedback.');
    }
  };

  return (
    <div className="container mt-5">
      <button onClick={() => handleSubmit("2 + 2 = 5")} className="btn btn-primary">
        Submit Sample Answer
      </button>
      {feedback && <div className="mt-3 alert alert-info">{feedback}</div>}
    </div>
  );
};

export default StudentPortal;