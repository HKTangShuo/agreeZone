// components/tabbar/tabbar.js
var auth = require('../../utils/auth.js')
Component({
  /**
   * 组件的属性列表
   */
  properties: {
    selected: {
      type: Number,
      value: 0
    }
  },
  /**
   * 组件的初始数据
   */
  data: {
    color: "#7A7E83",
    selectedColor: "#b4282d",
    list: [{
        "pagePath": "/pages/index/index",
        "text": "首页",
        "iconPath": "/static/images/tabbar/tab_home_normal.png",
        "selectedIconPath": "/static/images/tabbar/tab_home.png"
      },
      {
        "pagePath": "/pages/agreePoint/agreePoint",
        "text": "赞点",
        "iconPath": "/static/images/tabbar/tab_agreePoint_normal.png",
        "selectedIconPath": "/static/images/tabbar/tab_agreePoint.png"
      },
      {
        "text": "发布"
      },
      {
        "pagePath": "/pages/agreeBook/agreeBook",
        "text": "赞书",
        "iconPath": "/static/images/tabbar/tab_agreeBook_normal.png",
        "selectedIconPath": "/static/images/tabbar/tab_agreeBook.png"
      },
      {
        "pagePath": "/pages/home/home",
        "text": "我的",
        "iconPath": "/static/images/tabbar/tab_profile_normal.png",
        "selectedIconPath": "/static/images/tabbar/tab_profile.png"
      }
    ]
  },

  /**
   * 组件的方法列表
   */
  methods: {
    switchTab(e) {
      const data = e.currentTarget.dataset;
      const url = data.path;
      console.log(url)
      if(url=='/pages/home/home' && ! auth.authentication()){
       
        return
      }

      if (data.path) {
        wx.switchTab({
          url
        })
        return
      }
      var result = auth.authentication();
      if (result) {
        wx.navigateTo({
          url: '/pages/publish/publish',
        })
      }
    }
  }
})