import React, { useState } from 'react';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';

const TeacherPortal = () => {
  const [uploadStatus, setUploadStatus] = useState('');

  const { getRootProps, getInputProps } = useDropzone({
    accept: {'image/*': ['.png', '.jpg', '.jpeg'], 'application/pdf': ['.pdf']},
    onDrop: async (files) => {
      const formData = new FormData();
      formData.append('file', files[0]);
      try {
        await axios.post('http://localhost:8000/api/upload-notes', formData);
        setUploadStatus('Upload successful!');
      } catch (error) {
        setUploadStatus('Upload failed.');
      }
    },
  });

  return (
    <div className="container mt-5">
      <div {...getRootProps({ className: 'dropzone p-4 border rounded' })}>
        <input {...getInputProps()} />
        <p>Drag & drop notes (PDF/image) here, or click to select</p>
      </div>
      {uploadStatus && <p className="mt-3">{uploadStatus}</p>}
    </div>
  );
};

export default TeacherPortal;