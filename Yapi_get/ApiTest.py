

@request(url='/app/distribute/getDistributeSettings',method='POST')
def app_distribute_getDistributeSettings(self):
    """获取分销设置信息接口 (基础设置,特权说明，提现设置)"""
    json = {
        }
    return {'json': json, 'headers': self.headers}

@request(url='/app/distributor/flowList',method='POST')
def app_distributor_flowList(self, openId):
    """收支明细列表"""
    json = {
        "openId": openId,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/app/distributor/flowDetail',method='POST')
def app_distributor_flowDetail(self, sysnumber, openId):
    """收支明细详情"""
    json = {
        "sysnumber": sysnumber,
        "openId": openId,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/app/order/getList',method='POST')
def app_order_getList(self, openId, orderStatus, pageNum, pageSize):
    """我的订单列表"""
    json = {
        "openId": openId,
        "orderStatus": orderStatus,
        "pageNum": pageNum,
        "pageSize": pageSize,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/app/order/detail',method='POST')
def app_order_detail(self, sysnumber):
    """订单详情"""
    json = {
        "sysnumber": sysnumber,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/app/distribute/uploadFileOrigin',method='POST')
def app_distribute_uploadFileOrigin(self, file):
    """分销系统 图片原尺寸上传"""
    json = {
        "file": file,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/app/goods/getList',method='POST')
def app_goods_getList(self):
    """产品列表接口"""
    json = {
        }
    return {'json': json, 'headers': self.headers}

@request(url='/app/distribute/getRecentDistributorAccount',method='POST')
def app_distribute_getRecentDistributorAccount(self, openId, accountType):
    """ 获取最新的分销商支付账户接口"""
    json = {
        "openId": openId,
        "accountType": accountType,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/app/order/add',method='POST')
def app_order_add(self, openId, recvProvinceCode, recvCityCode, recvDistCode, contactAddress, contactPerson, contactWay, goods):
    """推客下单"""
    json = {
        "openId": openId,
        "recvProvinceCode": recvProvinceCode,
        "recvCityCode": recvCityCode,
        "recvDistCode": recvDistCode,
        "contactAddress": contactAddress,
        "contactPerson": contactPerson,
        "contactWay": contactWay,
        "goods": goods,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/app/order/getOrderWechatStatus',method='GET')
def app_order_getOrderWechatStatus(self):
    """微信小程序订单状态"""
    json = {
        }
    return {'json': json, 'headers': self.headers}

@request(url='/app/distributor/withdrawApply',method='POST')
def app_distributor_withdrawApply(self, withdrawAccount, accountType, accoutBank, withdrawAmount):
    """推客提现申请接口"""
    json = {
        "withdrawAccount": withdrawAccount,
        "accountType": accountType,
        "accoutBank": accoutBank,
        "withdrawAmount": withdrawAmount,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/app/distributor/goToPage',method='POST')
def app_distributor_goToPage(self, openId, code):
    """扫推客码中间跳转判断接口"""
    json = {
        "openId": openId,
        "code": code,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/app/distribute/getDistributorApply',method='POST')
def app_distribute_getDistributorApply(self, openId):
    """获取申请分销基本信息接口"""
    json = {
        "openId": openId,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/app/distribute/commitDistributorApply',method='POST')
def app_distribute_commitDistributorApply(self, openId, name, mobile, idCardNumber):
    """申请分销--基本信息提交接口"""
    json = {
        "openId": openId,
        "name": name,
        "mobile": mobile,
        "idCardNumber": idCardNumber,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/app/distributor/goToMemberPage',method='POST')
def app_distributor_goToMemberPage(self, openId, code):
    """扫会员码中间跳转判断接口"""
    json = {
        "openId": openId,
        "code": code,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/app/distributor/detail',method='POST')
def app_distributor_detail(self, sysnumber):
    """推客详情基本信息接口"""
    json = {
        "sysnumber": sysnumber,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/app/distributor/distributorWorkspace',method='POST')
def app_distributor_distributorWorkspace(self, openId):
    """推客工作台"""
    json = {
        "openId": openId,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/app/distributor/promotionDetail',method='POST')
def app_distributor_promotionDetail(self, openId, validMonth):
    """推客推广业绩详情"""
    json = {
        "openId": openId,
        "validMonth": validMonth,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/app/order/upFile',method='POST')
def app_order_upFile(self, openId, sysnumber, payWay, showPath):
    """上传支付凭证"""
    json = {
        "openId": openId,
        "sysnumber": sysnumber,
        "payWay": payWay,
        "showPath": showPath,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/app/order/getOrderPayWay',method='GET')
def app_order_getOrderPayWay(self):
    """支付枚举值"""
    json = {
        }
    return {'json': json, 'headers': self.headers}

@request(url='/app/order/receiveGoods',method='POST')
def app_order_receiveGoods(self, sysnumber, openId):
    """推客确认收货接口"""
    json = {
        "sysnumber": sysnumber,
        "openId": openId,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/app/order/deleteOrder',method='POST')
def app_order_deleteOrder(self, sysnumber, openId):
    """推客删除订单"""
    json = {
        "sysnumber": sysnumber,
        "openId": openId,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/app/distribute/getMiniQr',method='POST')
def app_distribute_getMiniQr(self, openId, scene, path):
    """获取二维码接口"""
    json = {
        "openId": openId,
        "scene": scene,
        "path": path,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/app/distributor/distributorPromotionList',method='POST')
def app_distributor_distributorPromotionList(self, openId, validMonth):
    """获取下级推客业绩分页列表接口"""
    json = {
        "openId": openId,
        "validMonth": validMonth,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/distribute/getDistributeSettings',method='POST')
def distribute_getDistributeSettings(self):
    """获取分销设置信息接口 (基础设置,特权说明，提现设置，软文)"""
    json = {
        }
    return {'json': json, 'headers': self.headers}

@request(url='/distribute/getDistributorLevelList',method='POST')
def distribute_getDistributorLevelList(self):
    """获取推客等级列表接口"""
    json = {
        }
    return {'json': json, 'headers': self.headers}

@request(url='/distribute/getVipList',method='POST')
def distribute_getVipList(self, pageNum, pageSize, name, startTime, endTime, distributerId, dieticianSysnumber, packageStatus, belongedSalesId):
    """获取会员列表"""
    json = {
        "pageNum": pageNum,
        "pageSize": pageSize,
        "name": name,
        "startTime": startTime,
        "endTime": endTime,
        "distributerId": distributerId,
        "dieticianSysnumber": dieticianSysnumber,
        "packageStatus": packageStatus,
        "belongedSalesId": belongedSalesId,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/distribute/getAllDistributerList',method='POST')
def distribute_getAllDistributerList(self):
    """获取上级推客列表（会员管理）"""
    json = {
        }
    return {'json': json, 'headers': self.headers}

@request(url='/members/stageStatus',method='POST')
def members_stageStatus(self):
    """获取疗程状态"""
    json = {
        }
    return {'json': json, 'headers': self.headers}

@request(url='/order/getList',method='POST')
def order_getList(self, pageNum, pageSize, name, startTime, endTime, orderStatus):
    """获取订单列表"""
    json = {
        "pageNum": pageNum,
        "pageSize": pageSize,
        "name": name,
        "startTime": startTime,
        "endTime": endTime,
        "orderStatus": orderStatus,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/order/orderStatus',method='POST')
def order_orderStatus(self):
    """获取订单枚举类"""
    json = {
        }
    return {'json': json, 'headers': self.headers}

@request(url='/order/pass',method='GET')
def order_pass(self):
    """订单审核通过"""
    json = {
        }
    return {'json': json, 'headers': self.headers}

@request(url='/order/deliverGoods',method='POST')
def order_deliverGoods(self, sysnumber, timeSend, showPath):
    """订单发货"""
    json = {
        "sysnumber": sysnumber,
        "timeSend": timeSend,
        "showPath": showPath,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/order/upFile',method='GET')
def order_upFile(self):
    """订单上传凭证"""
    json = {
        }
    return {'json': json, 'headers': self.headers}

@request(url='/order/notPass',method='GET')
def order_notPass(self):
    """订单驳回"""
    json = {
        }
    return {'json': json, 'headers': self.headers}

@request(url='/order/invalidOrder',method='POST')
def order_invalidOrder(self, sysnumber):
    """订单置为失效"""
    json = {
        "sysnumber": sysnumber,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/order/recoveryOrder',method='POST')
def order_recoveryOrder(self, sysnumber):
    """订单恢复"""
    json = {
        "sysnumber": sysnumber,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/order/deleteOrder',method='POST')
def order_deleteOrder(self, sysnumber):
    """订单删除"""
    json = {
        "sysnumber": sysnumber,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/order/getCash',method='GET')
def order_getCash(self):
    """订单确认收款"""
    json = {
        }
    return {'json': json, 'headers': self.headers}

@request(url='/order/sendCash',method='GET')
def order_sendCash(self):
    """订单打款"""
    json = {
        }
    return {'json': json, 'headers': self.headers}

@request(url='/distribute/uploadFileOrigin',method='POST')
def distribute_uploadFileOrigin(self, file):
    """分销系统 图片原尺寸上传"""
    json = {
        "file": file,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/distribute/updateDistributeSettings',method='POST')
def distribute_updateDistributeSettings(self, sysnumber, cutoffDay, salesRadio, articleTitle, articleContent, withdrawWay, withdrawMinimumAmount):
    """编辑分销设置接口 (基础设置,特权说明(软文)，提现设置)"""
    json = {
        "sysnumber": sysnumber,
        "cutoffDay": cutoffDay,
        "salesRadio": salesRadio,
        "articleTitle": articleTitle,
        "articleContent": articleContent,
        "withdrawWay": withdrawWay,
        "withdrawMinimumAmount": withdrawMinimumAmount,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/distributor/assignPage',method='POST')
def distributor_assignPage(self, keyword, applyStatus):
    """获取推客待分配接口"""
    json = {
        "keyword": keyword,
        "applyStatus": applyStatus,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/order/getOrderBackStatus',method='GET')
def order_getOrderBackStatus(self):
    """管理后台订单状态"""
    json = {
        }
    return {'json': json, 'headers': self.headers}

@request(url='/distributor/assignedPage',method='POST')
def distributor_assignedPage(self):
    """获取推客已分配接口"""
    json = {
        }
    return {'json': json, 'headers': self.headers}

@request(url='/distributor/audit',method='POST')
def distributor_audit(self, sysnumber, applyStatus, rejectReason):
    """总监审核推客接口"""
    json = {
        "sysnumber": sysnumber,
        "applyStatus": applyStatus,
        "rejectReason": rejectReason,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/distributor/assignSale',method='POST')
def distributor_assignSale(self, sysnumber, belongedSalesId):
    """总监指派推客业务员接口"""
    json = {
        "sysnumber": sysnumber,
        "belongedSalesId": belongedSalesId,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/distributor/listAudit',method='POST')
def distributor_listAudit(self):
    """获取 推客待审核接口（业务员）"""
    json = {
        }
    return {'json': json, 'headers': self.headers}

@request(url='/distributor/listPage',method='POST')
def distributor_listPage(self):
    """获取 已审核推客列表接口（业务员）"""
    json = {
        }
    return {'json': json, 'headers': self.headers}

@request(url='/distributor/enable',method='POST')
def distributor_enable(self, sysnumber, status):
    """推客停用 重新启用接口"""
    json = {
        "sysnumber": sysnumber,
        "status": status,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/distributor/addAppraise',method='POST')
def distributor_addAppraise(self, sysnumber, month, promotionCount, activityCount):
    """推客添加考核数据"""
    json = {
        "sysnumber": sysnumber,
        "month": month,
        "promotionCount": promotionCount,
        "activityCount": activityCount,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/distributor/detail',method='POST')
def distributor_detail(self, sysnumber):
    """推客详情接口（业务员调用）"""
    json = {
        "sysnumber": sysnumber,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/distributor/incomePage',method='POST')
def distributor_incomePage(self, sysnumber):
    """推客收入分页接口（业务员"""
    json = {
        "sysnumber": sysnumber,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/distributor/withdrawPage',method='POST')
def distributor_withdrawPage(self, sysnumber):
    """单个推客提现分页接口（业务员"""
    json = {
        "sysnumber": sysnumber,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/distributor/spreadPage',method='POST')
def distributor_spreadPage(self, sysnumber):
    """推客主动传播分页接口（业务员_copy"""
    json = {
        "sysnumber": sysnumber,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/distributor/withdrawList',method='POST')
def distributor_withdrawList(self):
    """推客提现分页接口（业务员"""
    json = {
        }
    return {'json': json, 'headers': self.headers}

@request(url='/distributor/withdrawAudit',method='POST')
def distributor_withdrawAudit(self, sysnumber, applyStatus):
    """推客提现审核接口（业务员调）"""
    json = {
        "sysnumber": sysnumber,
        "applyStatus": applyStatus,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/distributor/awardList',method='POST')
def distributor_awardList(self):
    """推客收益明细分页接口（业务员调"""
    json = {
        }
    return {'json': json, 'headers': self.headers}

@request(url='/distributor/withdrawFinanceList',method='POST')
def distributor_withdrawFinanceList(self, type):
    """推客提现分页接口（财务调用"""
    json = {
        "type": type,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/distributor/withdrawFinanceAudit',method='POST')
def distributor_withdrawFinanceAudit(self, sysnumber, applyStatus, rejectReason):
    """推客提现审核接口（财务调）"""
    json = {
        "sysnumber": sysnumber,
        "applyStatus": applyStatus,
        "rejectReason": rejectReason,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/excel/export',method='POST')
def excel_export(self):
    """excel文件模板导出"""
    json = {
        }
    return {'json': json, 'headers': self.headers}

@request(url='/excel/importExcel',method='POST')
def excel_importExcel(self):
    """excel文件导入"""
    json = {
        }
    return {'json': json, 'headers': self.headers}

@request(url='/order/detail',method='POST')
def order_detail(self, sysnumber):
    """订单详情"""
    json = {
        "sysnumber": sysnumber,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/order/financeAudit',method='POST')
def order_financeAudit(self, sysnumber, auditType, remark):
    """订单财务审核"""
    json = {
        "sysnumber": sysnumber,
        "auditType": auditType,
        "remark": remark,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/order/businessAudit',method='POST')
def order_businessAudit(self, sysnumber, auditType, remark):
    """订单业务审核"""
    json = {
        "sysnumber": sysnumber,
        "auditType": auditType,
        "remark": remark,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/distribute/removeDistributorLevel',method='POST')
def distribute_removeDistributorLevel(self, sysnumber):
    """逻辑删除推客等级"""
    json = {
        "sysnumber": sysnumber,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/distribute/updateDistributorLevel',method='POST')
def distribute_updateDistributorLevel(self, orderAmount, levelRank, sysnumber, promotionAward, promotionAwardUnit, promotionNumber, activityNumber, levelName):
    """编辑推客等级接口"""
    json = {
        "orderAmount": orderAmount,
        "levelRank": levelRank,
        "sysnumber": sysnumber,
        "promotionAward": promotionAward,
        "promotionAwardUnit": promotionAwardUnit,
        "promotionNumber": promotionNumber,
        "activityNumber": activityNumber,
        "levelName": levelName,
        }
    return {'json': json, 'headers': self.headers}

@request(url='/distribute/addDistributorLevel',method='POST')
def distribute_addDistributorLevel(self, orderAmount, levelRank, levelName, promotionAward, promotionAwardUnit, promotionNumber, activityNumber):
    """添加推客等级"""
    json = {
        "orderAmount": orderAmount,
        "levelRank": levelRank,
        "levelName": levelName,
        "promotionAward": promotionAward,
        "promotionAwardUnit": promotionAwardUnit,
        "promotionNumber": promotionNumber,
        "activityNumber": activityNumber,
        }
    return {'json': json, 'headers': self.headers}
