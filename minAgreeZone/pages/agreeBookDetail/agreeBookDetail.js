var api = require('../../config/api.js')
var app = getApp();

Page({

  /**
   * 页面的初始数据
   */
  data: {
    agreeBookDetail: {},
    agreeBookId: null
  },

  getDetailInfo:function(){
    var userInfo = app.globalData.userInfo;
    wx.request({
      url: api.AgreeBook + this.data.agreeBookId + '/',
      header: {
        Authorization: userInfo ? "token " + userInfo.token : ""
      },
      method: 'GET',
      dataType: 'json',
      responseType: 'text',
      success: (res) => {
        this.setData({
          agreeBookDetail: res.data
        })
      }
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function(options) {
    console.log(options)
    this.setData({
      agreeBookId: options.agreeBookId
    });
    
    this.getDetailInfo();
  },


  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function() {
    this.getDetailInfo();
  },




})