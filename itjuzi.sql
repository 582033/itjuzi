charset utf8;
drop table if exists company;
CREATE TABLE `company` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `juzi_id` varchar(30) NOT NULL COMMENT '公司在it桔子的ID',
  `company_name` varchar(120) default NULL COMMENT '公司名称',
  `company_sec_name` varchar(120) default NULL COMMENT '公司副名',
  `company_full_name` varchar(120) default NULL COMMENT '工商注册名称',
  `company_url` text default NULL COMMENT '公司网址',
  `company_tags` text default NULL COMMENT '公司TAG',
  `company_category` text default NULL COMMENT '公司分类',
  `company_slogan` text default NULL COMMENT '公司slogan',
  `company_description` text default NULL COMMENT '公司描述',
  `company_born` varchar(40) default NULL COMMENT '公司注册日期',
  `company_status` varchar(40) default NULL COMMENT '公司状态',
  `company_scale` varchar(40) default NULL COMMENT '公司规模',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

drop table if exists faild;
CREATE TABLE `faild` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `juzi_id` varchar(30) NOT NULL COMMENT '失败的it桔子ID',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
