<template>
    <div class="h-[93vh]">
        <div class="relative flex items-center p-3 border-b border-gray-300">
            CHAT TITLE
        </div>
        <div class="relative w-full p-6 overflow-y-auto">
            <ul class="space-y-2">
                <Message messageText="Test message"></Message>
            </ul>
        </div>
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