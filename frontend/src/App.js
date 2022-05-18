import React from 'react';
import { BrowserRouter as Router,Route,Routes } from 'react-router-dom';
import { ToastContainer } from 'react-bootstrap';
import HomePage from './pages/HomePage';
import PropertiesPage from './pages/PropertiesPage';
import {Footer} from './components/Footer';
import {Header}  from './components/Header'
import "react-toastify/dist/ReactToastify.css";
import NotFound from './components/NotFound';

const  App = () => {
  return (
    <>
    <Router>
      <Header/>
      <main className="py-3">
        <Routes>
          <Route path="/" element={<HomePage/>}></Route>
          <Route path="/properties" element={<PropertiesPage/>}></Route>
          <Route path='*' element={<NotFound/>}></Route>
        </Routes>
      <ToastContainer/>
      </main>
    </Router>

    </>

  );
}

export default App;
