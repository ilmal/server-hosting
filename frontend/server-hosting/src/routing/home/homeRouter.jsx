import React from "react"

import {
    Route,
    Routes
} from "react-router-dom"

import HomePage from "../../pages/home"

const HomeRouter = () => {
    return (
        <Routes>
            <Route exact path="/" element={<HomePage />} />
        </Routes>
    );
}

export default HomeRouter;