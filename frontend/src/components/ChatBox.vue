<template>
    <div class="relative flex items-center p-3 border-b border-gray-300">
        CHAT TITLE
    </div>
    <div class="relative w-full p-6 overflow-y-auto h-[40rem]">
        <ul class="space-y-2">
            <Message messageText="Test message"></Message>
        </ul>
    </div>
</template>

<script>
import Message from "./Message.vue"
export default {
  name: "ChatBox",
  components: {
    'Message': Message
  }
}
</script>