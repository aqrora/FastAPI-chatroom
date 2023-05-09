<template>
  <div class="border-r border-gray-300 lg:col-span-1">
    <div class="mx-3 my-3">  
    </div>

    <ul class="overflow-auto h-[32rem]">
      <h2 class="my-2 mb-2 ml-2 text-lg text-gray-600">Chats</h2>
        <li>
          <SidebarItem title="Hehe test" picture="https://images.pexels.com/photos/1170986/pexels-photo-1170986.jpeg"></SidebarItem>
        </li>
      </ul>
    </div>
</template>

<script>
import SidebarItem from "./SidebarItem.vue"
export default {
  name: "Sidebar",
  components: {
    'SidebarItem': SidebarItem
  }
}
</script>