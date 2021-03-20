<template>
    <nav class='navbar navbar-expand-lg navbar-light bg-light'>
        <router-link to='/'>DS Slideshow</router-link>

        <button class='navbar-toggler' type='button' data-toggle='collapse' data-target='#navbarContent'
                aria-controls='navbarSupportedContent' aria-expanded='false' aria-label='Toggle navigation'>
            <span class='navbar-toggler-icon'></span>
        </button>

        <div class='collapse navbar-collapse' id='navbarContent'>
            <ul class='navbar-nav ml-auto'>
                <li class='nav-item'>
                    <a class='nav-link'>
                        <i class='fas fa-cogs'></i>&ensp;Settings
                    </a>
                </li>

                <div>
                    <li class='nav-item'>
                        <a class='nav-link'>
                            <i class='fas fa-user-cog'></i>&nbsp;Profile
                        </a>
                    </li>

                    <li class='nav-item'>
                        <a class='nav-link'>
                            <i class='fas fa-sign-out-alt'></i>Sign&nbsp;Out
                        </a>
                    </li>
                </div>

                <li class='nav-item'>
                    <a class='nav-link' href='#'><i class='fab fa-'></i>Documentation</a>
                </li>

                <li class='nav-item'>
                    <a
                    class='nav-link fs-30 p-0' 
                    href='https://github.com/Digital-Signage-Slideshow/DS_Slideshow'
                    target='_blank'>
                        <i class='fab fa-github'></i>
                    </a>
                </li>
            </ul>
        </div>
    </nav>
</template>

<script>
    export default {
        name: 'Navbar',
        props: {
            currentUser: Object
        },
    }
</script>