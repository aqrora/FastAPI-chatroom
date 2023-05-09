
<template>

    <li v-bind:class = "(isMessageFromCurrentUser()) ? 'flex justify-end' : 'flex justify-start'">
        <div class="relative max-w-xl px-4 py-2 text-gray-700 rounded shadow"
        :class = "(!isMessageFromCurrentUser()) ? 'bg-gray-100' : ''">
            <span class="block">{{ messageText }}</span>
        </div>
    </li>
</template>

<script>
export default {
    props: [
        'messageText'
        // message id
        // is same author
        //'username',
        // 'avatar',
        // 'messageText',
        // 'date',
    ],
    methods: {
        isSameAuthor() {
            // TODO
            return true;
        },
        isMessageFromCurrentUser() {
            // TODO
            return false;
        }
    }
};
</script>
