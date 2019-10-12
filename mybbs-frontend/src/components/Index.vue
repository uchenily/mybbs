<template>
  <div>
    <common-header></common-header>
    <div class="select clearfix">
        <div :class="{hot:'hot', active:result.current=='hot'}" @click="active('hot')">热门</div>
        <div :class="{latest:'latest', active:result.current=='latest'}" @click="active('latest')">最新</div>
        <div :class="{agree:'agree', active:result.current=='agree'}" @click="active('agree')">点赞</div>
        <div :class="{trend:'trend', active:result.current=='all'}" @click="active('all')">趋势</div>
    </div>
    <common-content :items="result.items"></common-content>
  </div>
</template>

<script>
import axios from 'axios'
import Header from './common/Header'
import Content from './common/Content'
export default {
  name: 'Index',
  data: function() {
    return {
      result: {
        current: 'latest'
      }
    }
  },
  components: {
    CommonHeader: Header,
    CommonContent: Content
  },
  methods: {
    active (select) {
      axios.get('/api/v1/topics?flag=' + select)
      .then((response) => {
        if (response.data) {
          this.$set(this.result, "items", response.data)
          this.$set(this.result, "current", select)
          for (let [index, item] of this.result.items.entries()) {
            let topic_id = item.id
            axios.get('/api/v1/replies?topic_id=' + topic_id)
            .then((replies) => {
              if(replies.data && replies.data[0]) {
                this.$set(this.result.items[index], "latestReply", replies.data[0].content)
              }
            })
          }
        }
      })
    }
  },
  mounted: function () {
    this.active('latest')
  }
}
</script>

<style scoped>
.select {
    width: 70%;
    margin: 0 auto;
}
.select div {
    float: left;
    margin: -10px 40px 20px 0;
    padding: 16px 34px;
    color: #fff;
    font-size: 16px;
    font-weight: 700;
}
.select div.active {
    filter:alpha(Opacity=30);
    -moz-opacity:0.3;
    opacity: 0.3;
}
.select .hot {
    background: #ff3860;
}
.select .latest {
    background: #01d1b2;
}
.select .agree {
    background: #3faaf1;
}
.select .trend {
    background: #ff470f;
}
</style>
