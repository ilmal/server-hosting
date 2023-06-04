import React from "react"

import {
    BrowserRouter as Router,
    Route,
    Routes
} from "react-router-dom"

import HomePage from "../../pages/home"

const HomeRouter = () => {


    return (
        <Router>
            <Routes>
                <Route exact path="/" component={HomePage} />
            </Routes>
        </Router>
    );
}

export default HomeRouter;