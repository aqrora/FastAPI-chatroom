
<template>
  <LoginPrompt></LoginPrompt>
    <div class="border rounded lg:grid lg:grid-cols-6">
      <Sidebar></Sidebar>

      <div class="block lg:col-span-5">
            <ChatBox></ChatBox>
            <MessageInput></MessageInput>
      </div>
    </div>
</template>






<script setup>
import Sidebar from "./components/Sidebar.vue"
import ChatBox from "./components/ChatBox.vue"
import MessageInput from "./components/MessageInput.vue"
import LoginPrompt from "./components/LoginPrompt.vue";
</script>
