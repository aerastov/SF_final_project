import * as React from "react";
import { Routes, Route, Outlet, Link, NavLink } from "react-router-dom";
import '../styles/App.scss';


import Home from './Home.tsx';
import Account from './Account.tsx';
import NoMatch from './404.tsx';

export default function App() {
  return (
    <div>
        <div className='center_column'>
            <h1>Video Box</h1>
        </div>
        <Routes>
            <Route path="/" element={<Layout />}>
                <Route index element={<Home />} />
                <Route path="account" element={<Account />} />
                <Route path="*" element={<NoMatch />} />
            </Route>
        </Routes>
    </div>
  );
}

function Layout() {
  return (
    <div>

      <nav>

        <div className='main_menu'>
            <button className='button_main_menu'><NavLink className={({ isActive }) =>(isActive ? "active" : "normal")} to={'/'}>HOME</NavLink></button>
            <button className='button_main_menu'><NavLink className={({ isActive }) =>(isActive ? "active" : "normal")} to={'/account'}>Account</NavLink></button>
        </div>


      </nav>

      <hr />
      <Outlet />
    </div>
  );
}






























//
// import React from 'react';
// import { BrowserRouter as Router, Route, Routes, NavLink } from 'react-router-dom';
// import '../styles/App.scss';
//
//
// import Home from './Home';
// import About from './About';
// import Projects from './Projects';
//
//
// function App() {
// 	return (
// 		<Router>
// 		<div className='cover'>
// 		    <header>
//                 <div className='button'>
//                     <button><NavLink className={({ isActive }) =>(isActive ? "active" : "normal")} to={'/'}>HOME</NavLink></button>
// 					<button><NavLink className={({ isActive }) =>(isActive ? "active" : "normal")} to={'/about'}>ABOUT</NavLink></button>
// {/*                     <button><NavLink className={({ isActive }) =>(isActive ? "active" : "normal")} to={'/projects'}>PROJECTS</NavLink></button> */}
//                 </div>
// 			</header>
// 			<main>
// 			<div>
// 				<Routes>
// 				    <Route path="/" element={<Home />} />
// 					<Route exact path={'/about'} element={<About />} />
// {/* 					<Route exact path={'/projects'} element={<Projects />} /> */}
// 				</Routes>
// 			</div>
// 			</main>
// 		</div>
// 		</Router>
// 	);
// };
//
// export default App;
