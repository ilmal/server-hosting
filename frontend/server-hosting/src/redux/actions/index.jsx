

export const productInfo = async (dispatch) => {

    const data = {
        "basic": {
            price: "10",
            cpu: "1",
            mem: "2",
        },
        "normal": {
            price: "15",
            cpu: "2",
            mem: "10",
        },
        "premium": {
            price: "20",
            cpu: "3",
            mem: "15",
        }
    }

    dispatch({
        type: "PRODUCT_INFO",
        payload: data
    })
}

export const login = (name, pass, dispatch) => {
    // axios.post(`${ip_address}/user/login`, {
    //     withCredentials: true,
    //     name: name.toLowerCase(),
    //     password: pass
    // }).then(async (response) => {
    //     if (response.data.message === "Success!") {
    //         await checkUserAuth(dispatch)
    //         createMcConfig(dispatch)
    //         dispatch({
    //             type: "LOGIN",
    //             payload: {
    //                 loginAuth: response.data.loginAuth,
    //                 userID: response.data.userID
    //             }
    //         })
    //         window.location.reload();
    //         await loadBaseData()
    //     } else {
    //         console.log("response.data: ", response.data)
    //         dispatch({
    //             type: "ERR_MESSAGE",
    //             payload: response.data
    //         })
    //     }
    // })
}

export const signup = async (name, email, password, dispatch) => {
    // console.log("sending req to signup")
    // axios.post(`${ip_address}/user/insert`, {
    //     data: {
    //         name: name.toLowerCase(),
    //         email: email.toLowerCase(),
    //         password
    //     }
    // })
    //     .then(async (response) => {
    //         console.log("response from signup")
    //         if (response.data === "User created") {
    //             login(name, password, dispatch)
    //             dispatch({
    //                 type: "MESSAGE",
    //                 payload: response.data
    //             })
    //         } else {
    //             dispatch({
    //                 type: "ERR_MESSAGE",
    //                 payload: response.data
    //             })
    //         }
    //     })
}



// db.createUser(
//     {
//         user: "nils",
//         pwd: "pass123",
//         roles: ["root"]
//     })