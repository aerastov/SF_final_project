import React from 'react';
// import { BrowserRouter as Router, Route, Routes, NavLink } from 'react-router-dom';
import '../styles/App.scss';

import { NavLink } from 'react-router-dom';
import { createBrowserHistory } from 'history';
import { Router, Route, Switch, Redirect } from 'react-router-dom';
export const history = createBrowserHistory();

// import Home from './Home';
// import Login from './Login';
import { Login } from 'Login';
import { Home } from 'Home';

function App() {
	return (
		<Router>
		<div className='cover'>
		    <header>
                <div className='button'>
                    <button><NavLink className={({ isActive }) =>(isActive ? "active" : "normal")} to={'/'}>HOME</NavLink></button>
					<button><NavLink className={({ isActive }) =>(isActive ? "active" : "normal")} to={'/about'}>LOGIN</NavLink></button>
                </div>
			</header>
			<main>
			<div>

			    <Router history={history}>
                  <Switch>
                    <Route path="/" component={<Home />} />
                    <Route path={'/about'} component={<Login />} />
                  </Switch>
                </Router>
			</div>
			</main>
		</div>
		</Router>
	);
};

export default App;
