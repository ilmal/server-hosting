import {
    BrowserRouter as Router,
    Route,
    Routes
} from "react-router-dom"

import homeRouter from "./home/homeRouter"
import notFoundPage from "./misc/notFoundPage"

const HomeRouter = () => {
    return (
        <Router>
            <Routes>
                <Route exact path="/" component={homeRouter} />
                <Route path="*" component={notFoundPage} />
            </Routes>
        </Router>
    );
}

export default HomeRouter;