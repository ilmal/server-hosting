import React, { useState } from "react"
import ReactDOM from "react-dom/client"
import {
    BrowserRouter as Router,
    Route,
    Routes
} from "react-router-dom"
import "./scss/main.scss"
import { Provider } from "react-redux"
import store from "./store"

import Header from "./components/header/header"
import HomeRouter from "./routing/router"
import { Tooltips } from "./components/tooltips"
import { TopMessage } from "./components/topMessages/index"


const MainComponent = () => {
    return (
        <Provider store={store}>
            <Router>
                <TopMessage />
                <Header />
                <Routes>
                    <Route path="*" element={<HomeRouter/>} />
                </Routes>
                <Tooltips />
            </Router>
        </Provider>
    )
}


ReactDOM.createRoot(document.querySelector("#root")).render(
    <MainComponent />
)