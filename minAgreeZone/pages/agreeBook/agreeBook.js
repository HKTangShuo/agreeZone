// pages/message/message.js
var app = getApp();
var api = require('../../config/api.js')

Page({

  /**
   * 页面的初始数据
   */
  data: {
    agreeBookList: [],
    loading: false,
    minId: null,
    maxId: null,
  },
  /**
   * 分页获取数据
   */
  getAgreeBook: function (roll) {
    var condition = {};
    if (roll) {
      condition["minId"] = this.data.minId;
    }
    wx.request({
      url: api.AgreeBook,
      data: condition,
      method: 'GET',
      dataType: 'json',
      responseType: 'text',
      success: (res) => {
        console.log(res);
        if (res.statusCode == 200) {
          var resultLength = res.data.length;
          if (resultLength > 0) {
            this.setData({
              minId: res.data[resultLength - 1].id
            });
            if (!this.data.maxId) {
              this.setData({
                maxId: res.data[0].id
              });
            }
            this.setData({
              agreeBookList: this.data.agreeBookList.concat(res.data)
            });
          } else {
            wx.showToast({
              title: '已经到底了',
              icon: 'none'
            })
          }

        } else {
          wx.showToast({
            title: '获取数据失败',
            icon: 'none'
          })
        }
      }
    })

  },
  /**
   * 获取最新数据
   */
  getLatestAgreeBook: function () {
    if (!this.data.maxId) {
      this.getMessage();
      return
    }
    wx.request({
      url: api.AgreeBook,
      data: {
        maxId: this.data.maxId
      },
      method: 'GET',
      dataType: 'json',
      responseType: 'text',
      success: (res) => {
        // 把最新的数据插入到最前面
        if (res.statusCode == 200) {
          var result = res.data.reverse();
          if (result.length <= 0) {
            wx.showToast({
              title: '没有新数据了',
              icon: 'none'
            })
            return
          }
          this.setData({
            agreeBookList: result.concat(this.data.agreeBookList),
            maxId: result[0].id
          })
        }
      },
      complete: (res) => {
        wx.stopPullDownRefresh();
      },
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.getAgreeBook(false);
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
    this.getLatestAgreeBook()
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
    this.getAgreeBook(true);
  },
})