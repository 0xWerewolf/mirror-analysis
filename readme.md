思路1:  
1. 读取csv中每一个txhash
2. curl得到对应#eventlog页面
3. html找到 **title='amount (uint256 )'>**
4. 把后面数字读出，转为ETH
5. 写入total，统计完成

思路2:  
1. 读取所有合约交易的log，把其中topic是auctionEnded（0xc07c8c3aa4357ff71dbb73989298b2b27ad41a7216d9846113d7377a8e5f4158）的这些log的data项取出，得到amount，从16进制转为10进制
2. 写入csv，or直接写入total