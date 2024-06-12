# Generated by Django 4.2.7 on 2024-05-08 02:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("infra", "0013_damagereport_regulation_remove_infra_交通規制_infra_交通規制"),
    ]

    operations = [
        migrations.CreateModel(
            name="Approach",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "近接方法",
                    models.CharField(
                        choices=[
                            ("地上", "地上"),
                            ("梯子", "梯子"),
                            ("橋梁点検車", "橋梁点検車"),
                            ("高所作業車", "高所作業車"),
                            ("軌陸車", "軌陸車"),
                            ("ボート", "ボート"),
                            ("ロープアクセス", "ロープアクセス"),
                            ("ドローン", "ドローン"),
                            ("ファイバースコープ", "ファイバースコープ"),
                            ("画像解析", "画像解析"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LoadGrade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "等級",
                    models.CharField(
                        choices=[
                            ("不明", "不明"),
                            ("一等橋", "一等橋"),
                            ("二等橋", "二等橋"),
                            ("三等橋", "三等橋"),
                            ("その他", "その他"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LoadWeight",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "活荷重",
                    models.CharField(
                        choices=[
                            ("不明", "不明"),
                            ("A活荷重", "A活荷重"),
                            ("B活荷重", "B活荷重"),
                            ("TL-20", "TL-20"),
                            ("TL-14", "TL-14"),
                            ("TL-6", "TL-6"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Rulebook",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "適用示方書",
                    models.CharField(
                        choices=[
                            ("不明", "不明"),
                            ("平成29年 道路橋示方書", "平成29年 道路橋示方書"),
                            ("平成24年 道路橋示方書", "平成24年 道路橋示方書"),
                            ("平成14年 道路橋示方書", "平成14年 道路橋示方書"),
                            ("平成8年 道路橋示方書", "平成8年 道路橋示方書"),
                            ("平成5年 道路橋示方書", "平成5年 道路橋示方書"),
                            ("平成2年 道路橋示方書", "平成2年 道路橋示方書"),
                            ("昭和55年 道路橋示方書", "昭和55年 道路橋示方書"),
                            ("昭和53年 道路橋示方書", "昭和53年 道路橋示方書"),
                            ("昭和47年 道路橋示方書", "昭和47年 道路橋示方書"),
                            ("昭和43年 プレストレスコンクリート道路橋示方書", "昭和43年 プレストレスコンクリート道路橋示方書"),
                            ("昭和39年 鉄筋コンクリート道路橋示方書", "昭和39年 鉄筋コンクリート道路橋示方書"),
                            ("昭和31年 鋼道路橋設計示方書", "昭和31年 鋼道路橋設計示方書"),
                            ("昭和15年 鋼道路橋設計示方書案", "昭和15年 鋼道路橋設計示方書案"),
                            ("大正15年 道路構造に関する細則案", "大正15年 道路構造に関する細則案"),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Thirdparty",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "第三者点検",
                    models.CharField(
                        choices=[("有り", "有り"), ("無し", "無し")], max_length=50
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UnderCondition",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "路下条件",
                    models.CharField(
                        choices=[
                            ("河川", "河川"),
                            ("水路", "水路"),
                            ("湖沼", "湖沼"),
                            ("海洋", "海洋"),
                            ("道路", "道路"),
                            ("鉄道", "鉄道"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="infra",
            name="第三者点検の有無",
        ),
        migrations.RemoveField(
            model_name="infra",
            name="活荷重",
        ),
        migrations.RemoveField(
            model_name="infra",
            name="等級",
        ),
        migrations.RemoveField(
            model_name="infra",
            name="路下条件",
        ),
        migrations.RemoveField(
            model_name="infra",
            name="近接方法",
        ),
        migrations.RemoveField(
            model_name="infra",
            name="適用示方書",
        ),
        migrations.AlterField(
            model_name="regulation",
            name="交通規制",
            field=models.CharField(
                choices=[
                    ("無し", "無し"),
                    ("片側交互通行", "片側交互通行"),
                    ("車線減少", "車線減少"),
                    ("歩道規制", "歩道規制"),
                    ("通行止め", "通行止め"),
                ],
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="infra",
            name="第三者点検",
            field=models.ManyToManyField(to="infra.thirdparty"),
        ),
        migrations.AddField(
            model_name="infra",
            name="活荷重",
            field=models.ManyToManyField(to="infra.loadweight"),
        ),
        migrations.AddField(
            model_name="infra",
            name="等級",
            field=models.ManyToManyField(to="infra.loadgrade"),
        ),
        migrations.AddField(
            model_name="infra",
            name="路下条件",
            field=models.ManyToManyField(to="infra.undercondition"),
        ),
        migrations.AddField(
            model_name="infra",
            name="近接方法",
            field=models.ManyToManyField(to="infra.approach"),
        ),
        migrations.AddField(
            model_name="infra",
            name="適用示方書",
            field=models.ManyToManyField(to="infra.rulebook"),
        ),
    ]