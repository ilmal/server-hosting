import React, { useState } from "react"
import ReactDOM from "react-dom"
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
    const [loading, setLoading] = useState(true)

    React.useEffect(async () => {
        if (!loading) return
        setLoading(false)
    }, [loading])

    if (loading) {
        return (
            <h1 className="loadingText">Loading...</h1>
        )
    } else {
        return (
            <Provider store={store}>
                <Router>
                    <TopMessage />
                    <Header />
                    <Routes>
                        <Route path="/" component={HomeRouter} />
                    </Routes>
                    <Tooltips />
                </Router>
            </Provider>
        )
    }
}

ReactDOM.render(
    <MainComponent />
    , document.querySelector("#root")
)
