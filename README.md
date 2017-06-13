# After_django

GET
1. 定义一个名称为Article的model，里面有如下六个字段：文章图片地址(img)、文章标题(title)、文章内容(content)、浏览量(views)、点赞量(likes)、创建日期(createtime)
2. 通过 http://127.0.0.1:8000/admin 进入后台，添加至少九篇文章，补充相应文章的字段内容
3. 通过 http://127.0.0.1:8000/index 进入首页，默认激活“ALL”标签，显示后台添加的所有文章

POST
1. 补充名称为Comment的model，表示评论信息，添加如下字段: 作者名称（name），作者头像地址(avatar)，评论内容(content)，评论时间(createtime)。 注意：作者头像默认为static/images/default.png，评论时间自动添加当前时间。
2. 补充名称CommentForm的form，表示评论表单，添加如下字段：作者名称（name），评论内容(comment)
3. 给CommentForm表单添加一个「关键词过滤器」，凡是评论中出现在“发票”、“钱”等词语的都会引发表单报错「Your comment contains invalid words,please check it again.」
4. 给CommentForm表单添加一个「评论字数过滤器」，凡是评论内容字数少于4个，引发表单报错“not enough words”
5. 模板中补充评论相关的html内容，用于显示评论表单
6. 访问文章详情页面，能正常显示提交的评论内容

实现文章 url 的跳转
1.	在 urls.py 里修改 detail 的 url，使其能根据不同文章跳转到类似： detail/1 形式的 url 中
2.	在 view 中添加参数，从而获取每一页的文章
3.	在 template 里的详情页 html 里把写死的文章替换成动态的文章
4.	在 template 里的列表页实现跳转到详情页

让一个评论只属于一篇文章
1.	在 models.py 让 Comment 和 Article 是多对一关系，多个评论可以属于一个文章，并在 template 的详情页 html 和 views.py 实现相应改动


