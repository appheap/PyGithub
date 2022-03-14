from github.scaffold import Scaffold
from github.types import Repository, Response


class CreateOrganizationRepository(Scaffold):
    """
    Create an organization repository
    """

    def create_organization_repository(
            self,
            *,
            organization: str,
            name: str,
            description: str = None,
            homepage: str = None,
            private: bool = False,
            visibility: str = 'public',
            has_issues: bool = True,
            has_projects: bool = False,
            has_wiki: bool = True,
            is_template: bool = False,
            team_id: int = None,
            auto_init: bool = False,
            gitignore_template: str = None,
            license_template: str = None,
            allow_squash_merge: bool = True,
            allow_merge_commit: bool = True,
            allow_rebase_merge: bool = True,
            allow_auto_merge: bool = False,
            delete_branch_on_merge: bool = False,
    ) -> 'Response':
        """
        Creates a new repository in the specified organization. The authenticated user must be a member of the organization.

        :param organization:
            Name of the Organization

        :param name:
            Required. The name of the repository.

        :param description:
            A short description of the repository.

        :param homepage:
            A URL with more information about the repository.

        :param private:
            Whether the repository is private.

        :param visibility:
            Can be "public" or "private".
            If your organization is associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+,
            visibility can also be "internal". Note: For GitHub Enterprise Server and GitHub AE, this endpoint will only list repositories available to all users on the enterprise.

        :param has_issues:
            Either "true" to enable issues for this repository or "false" to disable them. Default:

        :param has_projects:
            Either "true" to enable projects for this repository or "false" to disable them.
            Note: If you're creating a repository in an organization that has disabled repository projects, the default is "false", and if you pass "true",
            the API returns an error.
            Default:

        :param has_wiki:
            Either "true" to enable the wiki for this repository or "false" to disable it.
            Default:

        :param is_template:
            Either "true" to make this repo available as a template repository or "false" to prevent it.

        :param team_id:
            The "id" of the team that will be granted access to this repository.
            This is only valid when creating a repository in an organization.

        :param auto_init:
            Pass "true" to create an initial commit with empty README.

        :param gitignore_template:
            Desired language or platform .gitignore template to apply.
            Use the name of the template without the extension. For example, "Haskell".

        :param license_template:
            Choose an open source license template that best suits your needs,
            and then use the license keyword as the license_template string. For example, "mit" or "mpl-2.0".

        :param allow_squash_merge:
            Either "true" to allow squash-merging pull requests, or "false" to prevent squash-merging.
            Default:

        :param allow_merge_commit:
            Either "true" to allow merging pull requests with a merge commit, or "false" to prevent merging pull requests with merge commits.
            Default:

        :param allow_rebase_merge:
            Either "true" to allow rebase-merging pull requests, or "false" to prevent rebase-merging.
            Default:

        :param allow_auto_merge:
            Either "true" to allow auto-merge on pull requests, or "false" to disallow auto-merge.

        :param delete_branch_on_merge:
            Either "true" to allow automatically deleting head branches when pull requests are merged, or "false" to prevent automatic deletion.

        :return: 'Response' #todo: add return docstring
        """
        response = self.post_with_token(
            url=f'https://api.github.com/orgs/{organization}/repos',
            data={
                'name': name,
                'description': description,
                'homepage': homepage,
                'private': private,
                'visibility': visibility,
                'has_issues': has_issues,
                'has_projects': has_projects,
                'has_wiki': has_wiki,
                'is_template': is_template,
                'team_id': team_id,
                'auto_init': auto_init,
                'gitignore_template': gitignore_template,
                'license_template': license_template,
                'allow_squash_merge': allow_squash_merge,
                'allow_merge_commit': allow_merge_commit,
                'allow_rebase_merge': allow_rebase_merge,
                'allow_auto_merge': allow_auto_merge,
                'delete_branch_on_merge': delete_branch_on_merge,
            }
        )

        if response.status_code == 201:
            return Response._parse(
                response=response,
                success=True,
                result=Repository._parse(response.json())
            )
        elif response.status_code in (403, 422,):
            return Response._parse(
                response=response,
                success=False,
            )
        else:
            return Response._parse(
                response=response,
                success=False,
            )
