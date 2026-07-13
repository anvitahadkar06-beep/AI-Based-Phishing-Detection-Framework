function Navbar(){

    return(

        <nav
            style={{
                width:"100%",
                maxWidth:"900px",
                display:"flex",
                justifyContent:"space-between",
                alignItems:"center",
                marginBottom:"40px"
            }}
        >

            <h2
    style={{
        margin:0,
        display:"flex",
        alignItems:"center",
        gap:"10px"
    }}
>

    🛡️

    PhishGuard AI

</h2>

            <span style={{color:"#cbd5e1"}}>
                AI Powered Detection
            </span>

        </nav>

    )

}

export default Navbar;