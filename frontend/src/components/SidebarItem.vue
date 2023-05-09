<template>


    <a
        class="flex items-center px-3 py-2 text-sm transition duration-150 ease-in-out border-b border-gray-300 cursor-pointer hover:bg-gray-100 focus:outline-none">
        <img class="object-cover w-10 h-10 rounded-full"
            :src=picture alt="username" />
        <div class="w-full pb-2">
            <div class="flex justify-between">
            <span class="block ml-2 font-semibold text-gray-600">Chat theme</span>
            </div>
        </div>
    </a>


</template>

<script>
export default {
    props: [
        'title',
        'picture'
    ]
}
</script>