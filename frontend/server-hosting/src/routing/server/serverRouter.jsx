import {
    Route,
    Routes
} from "react-router-dom"

import MinecraftCreate from "../../pages/serverCreate/minecraft/minecraft"

const userRouter = () => {
    console.log("I'm here!!")
    return (
        <Routes>
            <Route path="/minecraft" element={<MinecraftCreate />} />
        </Routes>
    );
}

export default userRouter;