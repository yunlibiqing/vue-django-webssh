<template>
    <div>
        <web-ssh :socketURI="socketURI"></web-ssh>
    </div>
</template>

<script>
import 'xterm/css/xterm.css'
import WebSSH from './WebSSH.vue'

export default {
  name: 'Term',
  components: {
    'web-ssh': WebSSH
  },
  data () {
    return {
      socketURI: 'ws://127.0.0.1:9090/webssh/'
    }
  },
  methods: {
  }
}
</script>
