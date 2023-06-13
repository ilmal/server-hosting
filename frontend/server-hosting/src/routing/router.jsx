import {
    BrowserRouter as Router,
    Route,
    Routes
} from "react-router-dom"

import HomeRouterComponent from "./home/homeRouter"
import NotFoundPage from "./misc/notFoundPage"
import ServerRouter from "./server/serverRouter"

const HomeRouter = () => {
    return (
        <>
        <Routes>
            <Route exact path="/" element={<HomeRouterComponent/>} />
            <Route exact path="/server" element={<ServerRouter />} />
            <Route exact path="/server/*" element={<ServerRouter />} />
            <Route path="*" element={<NotFoundPage/>} />
        </Routes>
        </>

    );
}

export default HomeRouter;