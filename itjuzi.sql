charset utf8;
drop table itjuzi;
CREATE TABLE `itjuzi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `juzi_id` varchar(30) NOT NULL COMMENT '公司在it桔子的ID',
  `company_name` varchar(120) NOT NULL COMMENT '公司名称',
  `company_sec_name` varchar(120) NOT NULL COMMENT '公司副名',
  `company_full_name` varchar(120) NOT NULL COMMENT '工商注册名称',
  `company_url` text NOT NULL COMMENT '公司网址',
  `company_slogan` text NOT NULL COMMENT '公司slogan',
  `company_discription` text DEFAULT NULL COMMENT '公司描述',
  `company_born` text varchar(40) NULL COMMENT '公司注册日期',
  `company_status` text varchar(40) NULL COMMENT '公司状态',
  `company_category` text DEFAULT NULL COMMENT '公司分类',
  `company_tag` text DEFAULT NULL COMMENT '公司TAG',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
