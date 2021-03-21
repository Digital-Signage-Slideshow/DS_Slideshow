<template>
    <nav class='navbar navbar-expand-lg navbar-light bg-light'>
        <router-link to='/'>DS Slideshow</router-link>

        <button class='navbar-toggler' type='button' data-toggle='collapse' data-target='#navbarContent'
                aria-controls='navbarSupportedContent' aria-expanded='false' aria-label='Toggle navigation'>
            <span class='navbar-toggler-icon'></span>
        </button>

        <div class='collapse navbar-collapse' id='navbarContent'>
            <ul v-if='authenticated' class='navbar-nav ml-auto'>
                <li class='nav-item cursor-pointer'>
                    <a class='nav-link'>
                        <i class='fas fa-cogs'></i>Settings
                    </a>
                </li>

                <li class='nav-item cursor-pointer'>
                    <a class='nav-link'>
                        <i class='fas fa-user-cog'></i>Profile
                    </a>
                </li>


                <li class='nav-item cursor-pointer'>
                    <a class='nav-link' href='#'><i class='fab fa-'></i>GitHub</a>
                </li>

                <li class='nav-item cursor-pointer'>
                    <a class='nav-link text-danger'>Sign Out</a>
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

<style scoped>
    .cursor-pointer {
        cursor: pointer;
    }
</style>

<script>
    export default {
        name: 'Navbar',
        data() {
            return {
                authenticated: this.$store.getters.isAuthenticated,
            }
        },
    }
</script>