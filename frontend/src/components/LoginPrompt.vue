<template>
    <div class="fixed top-0 left-0 w-full h-full bg-black bg-opacity-50 backdrop-filter backdrop-blur-md z-50">
    <div id="loginPrompt" :class="{ hidden: !isSignIn }">
            <div class="fixed top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-gray-400 rounded-lg p-10 z-50 shadow-lg w-96">
            <div class="flex w-auto justify-center">
                <p class="mb-5 font-extrabold text-xl">Sign in</p>
            </div>
            <div class="flex flex-col mb-4">
                <input class="border-none rounded-md bg-gray-200 py-3 px-4 text-lg mb-2" type="text" maxlength="32" v-model="username" placeholder="Username">
                <input class="border-none rounded-md bg-gray-200 py-3 px-4 text-lg mb-2" type="password" maxlength="32" v-model="password" placeholder="Password">
                <button class="my-3 bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-4 rounded">Login</button>
            </div>
            <div class="flex w-auto justify-center">

                <p>Don't have an account? <a class="underline font-bold" href="#signUp" v-on:click="isSignIn = !isSignIn">Register one</a></p>  
            </div>
            </div>
    </div>
    <div id="registerPrompt" :class="{ hidden: isSignIn }">
        
            <div class="fixed top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-gray-400 rounded-lg p-10 z-50 shadow-lg w-96">
            <div class="flex w-auto justify-center">
                <p class="mb-5 font-extrabold text-xl">Sign up</p>
            </div>
            <div class="flex flex-col mb-4">
                <input class="border-none rounded-md bg-gray-200 py-3 px-4 text-lg mb-2" type="text" maxlength="32" v-model="username" placeholder="Username">
                <input class="border-none rounded-md bg-gray-200 py-3 px-4 text-lg mb-2" type="password" maxlength="32" v-model="password" v-on:input="comparePasswords()" placeholder="Password">
                <input class="border-none rounded-md bg-gray-200 py-3 px-4 text-lg mb-2" type="password" maxlength="32" v-model="confirmPassword" v-on:input="comparePasswords()" placeholder="Confirm Password">
                <span class="text-red-900 text-sm font-medium" :class="{ hidden: !matchErrorVisible }">Passwords don't match!</span>
                <button class="my-3 bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-4 rounded">Sign up</button>
            </div>
            <div class="flex w-auto justify-center">
                <p>Have an account? <a class="underline font-bold" href="#signin" v-on:click="isSignIn = !isSignIn">Log in</a></p>  
            </div>
            </div>
        
    </div>
    </div>
</template>


<script>
export default {
    methods: {
        comparePasswords() {
            if (this.password == "" || this.confirmPassword == "") {
                this.matchErrorVisible = false;
                return;
            }

            if (this.password === this.confirmPassword) {
                this.matchErrorVisible = false;
                return;
            } 

            this.matchErrorVisible = true;
            
        },
        submitForm() {
            // TODO
        }
        
    },
    data: function () {
        return {
            isSignIn: true,
            username: "",
            password: "",
            confirmPassword: "",
            matchErrorVisible: false
        };
    },



}
</script>