<?php
require __DIR__ . '/vendor/autoload.php';
ini_set('display_errors', 'On');
error_reporting(E_ALL ^ E_NOTICE);

class company{
    public $db;
    public function __construct(){
        $this->db = new \Simplon\Mysql\Mysql( 'localhost', 'root', '', 'itjuzi');
    }

    public function show(){
        $sql = "select * from company";
        $conds = array();
        $result = $this->db->fetchRowMany($sql, $conds);

        foreach($result as $k => $v){
            $tags = json_decode($v['company_tags']);
            $category = json_decode($v['company_category']);
            $result[$k]['company_tags'] = $tags;
            $result[$k]['company_category'] = $category;
        }
        #echo "<pre>";var_dump($result);exit;
        $json = json_encode($result);
        return $json;
    }

}

$company = new company();
$json = $company->show();
print_r($json);
