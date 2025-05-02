function Login() {

    const handleSubmit => (e) = {

    }

    return (
        <>
            <div>
                <div>
                    <form action="http://localhost:8000/login" method="get">
                        <label htmlFor="email">E-Mail</label>
                        <input type="text" id="email"/>

                        <label htmlFor="username">Username</label>
                        <input type="text" id="username" />

                        <label htmlFor="password">Password</label>
                        <input type="text" id="password" />

                        <button type="submit" className="bg-black text-white">Login</button>
                    </form>
                </div>
            </div>
        </>
    );
}

export default Login;