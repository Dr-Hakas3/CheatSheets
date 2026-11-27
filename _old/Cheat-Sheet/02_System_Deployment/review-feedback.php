<?php
/*
Plugin Name: Product Review Feedback
Description: 簡易的な商品レビュー投稿機能を提供します。
Version: 1.0
Author: Sample Dev
*/

add_shortcode('product_review_form', 'product_review_form_func');
add_action('init', 'product_review_form_handle');

function product_review_form_func() {
    ob_start();
    ?>
    <form method="post">
        <input type="text" name="review_name" placeholder="お名前" required><br>
        <textarea name="review_comment" placeholder="レビューを入力してください" required></textarea><br>
        <input type="submit" name="review_submit" value="投稿する">
    </form>
    <?php

    $reviews = get_option('product_reviews', []);
    foreach ($reviews as $r) {
        echo "<hr><strong>{$r['name']}</strong><br>{$r['comment']}";
    }

    return ob_get_clean();
}

function product_review_form_handle() {
    if (isset($_POST['review_submit'])) {
        $reviews = get_option('product_reviews', []);
        $reviews[] = [
            'name' => $_POST['review_name'],
            'comment' => $_POST['review_comment'],
        ];
        update_option('product_reviews', $reviews);
    }
}