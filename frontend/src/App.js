import React from 'react';
import { BrowserRouter as Router,Route,Routes } from 'react-router-dom';
import { ToastContainer } from 'react-bootstrap';
import HomePage from './pages/HomePage';
import PropertiesPage from './pages/PropertiesPage';
import {Footer} from './components/Footer';
import {Header}  from './components/Header'


const  App = () => {
  return (
    <>
    <Router>
      <Header/>
      <main className="py-3">
        <Routes>
          <Route path="/" element={<HomePage/>}></Route>
         <Route path="/properties" element={<PropertiesPage/>}></Route>
        </Routes>
      </main>
    </Router>

    <ToastContainer/>
    </>

  );
}

export default App;
