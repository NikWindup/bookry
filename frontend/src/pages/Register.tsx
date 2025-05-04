function Register() {

    const handleSubmit = () => {
        
    }

    return (
        <>
            <div>
                <div>
                    <form action="http://localhost:8000/register" method="post">
                        <label htmlFor="email">E-Mail</label>
                        <input type="text" id="email" />

                        <label htmlFor="username">Username</label>
                        <input type="text" id="username" />

                        <label htmlFor="password">Password</label>
                        <input type="text" id="password" />

                        <button type="submit" className="bg-black text-white" onClick={handleSubmit}>Login</button>
                    </form>
                </div>
            </div>
        </>
    );
}

export default Register;