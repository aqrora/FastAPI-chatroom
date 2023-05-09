
<template>
   <div class="container mx-auto">
      <div class="min-w-full border rounded lg:grid lg:grid-cols-3">
        <Sidebar></Sidebar>

        <div class="block lg:col-span-2">
              <ChatBox></ChatBox>
              <MessageInput></MessageInput>
            
        </div>
      </div>
    </div>
  <!-- <div class="bg-red-500">Hehe cats</div>
  <ul class="space-y-1 grid grid-cols-1">
    <Message message-text="hehe cats" username="username" avatar="avatar" date="date"/>
  </ul> -->
</template>






<script setup>
import Message from "./components/Message.vue"
import Sidebar from "./components/Sidebar.vue"
import ChatBox from "./components/ChatBox.vue"
import MessageInput from "./components/MessageInput.vue"
</script>
