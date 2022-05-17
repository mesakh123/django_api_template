import React from 'react'

export default function Spinner() {
  return (
    <div className="spinner-container">
        <Spinner animation="border" role="status">
          <span className="visually-hidden">Loading...</span>
        </Spinner>
    </div>
  )
}
